	.file	"target0.c"
	.text
	.globl	check_fail
	.def	check_fail;	.scl	2;	.type	32;	.endef
	.seh_proc	check_fail
check_fail:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$64, %rsp
	.seh_stackalloc	64
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	leaq	-32(%rbp), %rax
	movq	16(%rbp), %rdx
	movq	%rax, %rcx
	call	strcpy
	movl	$1, %eax
	addq	$64, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
.LC0:
	.ascii "target0: argc != 2\12\0"
.LC1:
	.ascii "Grade = %c\12\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$56, %rsp
	.seh_stackalloc	56
	leaq	128(%rsp), %rbp
	.seh_setframe	%rbp, 128
	.seh_endprologue
	movl	%ecx, -48(%rbp)
	movq	%rdx, -40(%rbp)
	call	__main
	cmpl	$2, -48(%rbp)
	je	.L4
	movl	$2, %ecx
	movq	__imp___acrt_iob_func(%rip), %rax
	call	*%rax
	movq	%rax, %r9
	movl	$19, %r8d
	movl	$1, %edx
	leaq	.LC0(%rip), %rcx
	call	fwrite
	movl	$1, %ecx
	call	exit
.L4:
	movq	-40(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	check_fail
	testl	%eax, %eax
	je	.L5
	movb	$70, -81(%rbp)
	jmp	.L6
.L5:
	movb	$65, -81(%rbp)
.L6:
	movsbl	-81(%rbp), %ebx
	movl	$1, %ecx
	movq	__imp___acrt_iob_func(%rip), %rax
	call	*%rax
	movl	%ebx, %r8d
	leaq	.LC1(%rip), %rdx
	movq	%rax, %rcx
	call	fprintf
	movl	$0, %eax
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (x86_64-posix-seh-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	strcpy;	.scl	2;	.type	32;	.endef
	.def	fwrite;	.scl	2;	.type	32;	.endef
	.def	exit;	.scl	2;	.type	32;	.endef
	.def	fprintf;	.scl	2;	.type	32;	.endef
